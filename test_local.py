#!/usr/bin/env python3
"""
Simple test script to verify OpenRouter integration works locally
Run this before pushing to Windmill to catch any issues early
"""

import os
import sys
import json

# Try to load .env file
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load .env file if it exists
    print("🔍 Debug: dotenv loaded successfully")
except ImportError:
    print("🔍 Debug: dotenv not available, using environment variables only")

def test_local():
    """Test the movie mood generator locally"""
    
    # Debug: Check current directory and .env file
    print(f"🔍 Debug: Current directory: {os.getcwd()}")
    print(f"🔍 Debug: .env file exists: {os.path.exists('.env')}")
    
    # Check if API key is set
    api_key = os.getenv("OPENROUTER_API_KEY")
    print(f"🔍 Debug: API key found: {'Yes' if api_key else 'No'}")
    
    if not api_key:
        print("❌ OPENROUTER_API_KEY not found or empty")
        print("Set it in one of these ways:")
        print("  1. Create .env file with: OPENROUTER_API_KEY=your-key-here")
        print("  2. Export env var: export OPENROUTER_API_KEY='your-key-here'")
        
        # Check if .env exists and show its content (without exposing secrets)
        if os.path.exists('.env'):
            print("🔍 .env file exists. Contents (keys only):")
            with open('.env', 'r') as f:
                for line_num, line in enumerate(f, 1):
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key = line.split('=')[0] if '=' in line else line
                        print(f"  Line {line_num}: {key}=...")
        
        return False
    
    print("🧪 Testing OpenRouter Movie Mood Generator...")
    print("=" * 50)
    
    try:
        # Import and test the main function
        from movie_mood_generator import main
        
        # Test with a few different movies
        test_movies = ["The Matrix", "Inception", "Pulp Fiction"]
        
        for movie in test_movies:
            print(f"\n🎬 Testing: {movie}")
            result = main(movie)
            
            if result.get('success'):
                print(f"✅ Success: {result['moods']}")
            else:
                print(f"❌ Failed: {result.get('error', 'Unknown error')}")
                return False
        
        print("\n" + "=" * 50)
        print("🎉 All tests passed! Ready for Windmill deployment.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure you're in the correct directory with movie_mood_generator.py")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = test_local()
    sys.exit(0 if success else 1)
