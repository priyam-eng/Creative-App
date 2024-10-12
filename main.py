import openai


openai.api_key = "your_openai_api_key_here"


def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"  
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        return f"Error occurred: {str(e)}"
    


      