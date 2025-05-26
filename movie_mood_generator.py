import requests
import json
import wmill
import os
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load .env file if it exists
except ImportError:
    pass  # dotenv not installed, skip

def main(movie_title: str = "The Matrix") -> dict:
    """
    Simple OpenRouter test: Generate mood words for a movie using OpenRouter API
    Args:
        movie_title: Name of the movie
    Returns:
        Dictionary with movie title and generated moods
    """
    
    # Get OpenRouter API key - try multiple sources
    api_key = None
    
    # First try environment variable (for local testing)
    api_key = os.getenv("OPENROUTER_API_KEY")
    
    # If not found in env, try Windmill resource
    if not api_key:
        try:
            # Get OpenRouter resource - try different paths silently
            openrouter_resource = None
            for resource_path in ["u/philipgalebach/thinner_openrouter", "philipgalebach/thinner_openrouter"]:
                try:
                    openrouter_resource = wmill.get_resource(resource_path)
                    break  # Found it, stop trying
                except:
                    continue  # Try next path
            # Handle both string and dict resource formats
            if openrouter_resource:
                if isinstance(openrouter_resource, dict):
                    api_key = openrouter_resource.get("api_key")
                else:
                    api_key = openrouter_resource
        except Exception:
            pass  # wmill might not be available in local testing
    
    if not api_key:
        return {
            "movie": movie_title,
            "error": "OpenRouter API key not found. Set OPENROUTER_API_KEY env var or configure Windmill resource.",
            "success": False
        }
    
    # Simple prompt for mood generation
    prompt = f"Generate 3-5 mood words that describe the movie '{movie_title}'. Return only the mood words separated by commas. Examples: Dark, Mysterious, Intense, Complex, Thought-provoking"
    
    try:
        # Make OpenRouter API call
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": "https://windmill.dev",  # Optional. Site URL for rankings
                "X-Title": "Windmill Movie Mood Generator",  # Optional. Site title for rankings
            },
            data=json.dumps({
                "model": "google/gemini-2.0-flash-lite-001",  # Using the model from your example
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                "max_tokens": 100,
                "temperature": 0.7
            })
        )
        
        # Check if request was successful
        response.raise_for_status()
        
        # Parse response
        response_data = response.json()
        moods = response_data['choices'][0]['message']['content'].strip()
        
        return {
            "movie": movie_title,
            "moods": moods,
            "model_used": "google/gemini-2.0-flash-lite-001",
            "success": True
        }
        
    except requests.exceptions.RequestException as e:
        return {
            "movie": movie_title,
            "error": f"Request error: {str(e)}",
            "success": False
        }
    except KeyError as e:
        return {
            "movie": movie_title,
            "error": f"Response parsing error: {str(e)}",
            "response": response.text if 'response' in locals() else "No response",
            "success": False
        }
    except Exception as e:
        return {
            "movie": movie_title,
            "error": f"Unexpected error: {str(e)}",
            "success": False
        }

# Test function for local development
if __name__ == "__main__":
    # Test locally with .env file or environment variable
    result = main("Inception")
    print(json.dumps(result, indent=2))
