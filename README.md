# Windmill + OpenRouter Movie Mood Generator

A Windmill workflow that generates mood words for movies using OpenRouter's API and Google's Gemini model.

## 🚀 Quick Start

### 1. Clone and Setup

```bash
git clone <your-repo>
cd windmill-test
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API Keys

#### For Local Development:
```bash
# Copy template and add your key
cp .env.template .env
# Edit .env and replace 'your_openrouter_api_key_here' with your actual key
```

#### For Windmill Deployment:
```bash
# Copy template and add your key
cp thinner_openrouter.resource.template.yaml thinner_openrouter.resource.yaml
# Edit the resource file and replace 'YOUR_OPENROUTER_API_KEY_HERE' with your actual key
```

### 3. Get Your OpenRouter API Key

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up/Login
3. Generate an API key
4. Add it to your `.env` and/or resource file

### 4. Test Locally

```bash
python movie_mood_generator.py
```

### 5. Deploy to Windmill

```bash
wmill sync push
```

## 🧪 Usage

### Command Line Test:
```bash
wmill script run u/philipgalebach/movie_mood_generator --data '{"movie_title": "Star Wars"}'
```

### Expected Output:
```json
{
  "moods": "Hopeful, Adventurous, Epic, Exciting, Nostalgic",
  "movie": "Star Wars", 
  "success": true,
  "model_used": "google/gemini-2.0-flash-lite-001"
}
```

## 🔐 Security Notes

- **Never commit actual API keys** - they are gitignored
- **Use template files** - these are safe to commit
- **Environment variables** - The code automatically detects local vs Windmill environment
- **Fallback logic** - Tries multiple resource paths for Windmill compatibility

## 📁 Project Structure

```
windmill-test/
├── movie_mood_generator.py              # Main script
├── requirements.txt                     # Dependencies
├── .env.template                        # Template for local dev
├── thinner_openrouter.resource.template.yaml  # Template for Windmill resource
├── u/philipgalebach/                   # Windmill deployment files
└── README.md                           # This file
```

## 🔧 Dependencies

- `requests==2.32.3` - HTTP requests
- `wmill==1.492.1` - Windmill SDK
- `python-dotenv` - Load .env files (optional)

## 🎬 API Details

- **Model**: `google/gemini-2.0-flash-lite-001`
- **Provider**: OpenRouter
- **Input**: Movie title string
- **Output**: Comma-separated mood words

## 🚨 Troubleshooting

### "API key not found" error:
- Check your `.env` file has the correct key
- Verify the resource file is properly configured in Windmill
- Make sure you're using the correct resource path

### "404 Not Found" in Windmill:
- Run `wmill sync push` to deploy your changes
- Check the resource exists in Windmill UI

## 🛠️ Development

The code is designed to work in both environments:
- **Local**: Uses `.env` file and environment variables
- **Windmill**: Uses Windmill resources with fallback logic

Safe to commit, ready for collaboration! 🎉
