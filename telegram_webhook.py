import wmill
import json
from telegram_movie_bot import main as handle_telegram_update

def main(body: dict) -> dict:
    """
    Webhook endpoint for Telegram bot
    
    This script receives webhook POSTs from Telegram and processes them.
    Set this as your Telegram webhook URL in Windmill.
    
    Args:
        body: Raw webhook request body from Telegram
    
    Returns:
        Dict with processing status
    """
    
    try:
        print(f"Received Telegram webhook: {json.dumps(body, indent=2)}")
        
        # Get Telegram resource
        telegram_auth = wmill.get_resource("u/philipgalebach/windmill_telegram_test2_bot")
        
        # Process the Telegram update
        result = handle_telegram_update(telegram_auth, body)
        
        print(f"Bot handler result: {json.dumps(result, indent=2)}")
        
        return {
            "status": "webhook_processed",
            "result": result,
            "webhook_body": body
        }
        
    except Exception as e:
        print(f"Webhook processing error: {str(e)}")
        return {
            "status": "webhook_error",
            "error": str(e),
            "webhook_body": body
        }


# For testing webhook locally (won't work without proper setup)
if __name__ == "__main__":
    test_webhook_body = {
        "update_id": 123,
        "message": {
            "message_id": 1,
            "from": {
                "id": 123456789,
                "is_bot": False,
                "first_name": "Test"
            },
            "chat": {
                "id": 123456789,
                "first_name": "Test",
                "type": "private"
            },
            "date": 1234567890,
            "text": "Inception"
        }
    }
    
    print("Telegram Webhook Handler - Test body:")
    print(json.dumps(test_webhook_body, indent=2))
