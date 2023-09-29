APP_GEOMETRY = "532x632"
APP_TITLE = "Text to Image app"
APP_BACKGROUND = 'black'
APP_APPERANCE_MODE = "dark" 

# Create input box on the user interface 
PROMPT_BOX_INTERFACE = {'height':40, 
                        'width':512, 
                        'text_font': ("Arial", 15), 
                        'text_color':"white", 
                        'fg_color':"black"} 

PROMPT_BOX_PLACE_COOR = {'x':10, 'y':10}

# Create a placeholder to show the generated image
IMAGE_PLACEHOLDER_INTERFACE = {'height':512, 'width':512, 'text':""}
IMAGE_PLACEHOLDER_COOR = {'x':10, 'y':110}

# Stable diffusion model from hugging face 
MODELID = "CompVis/stable-diffusion-v1-4"
REVISION = "fp16"
DEVICE = "cuda"
GUIDANCE_SCALE = 8.5

TRIGGER_BUTTON_INTERFACE = {'height':40, 
                            'width':120, 
                            'text_font': ("Arial", 15), 
                            'text_color':"black", 
                            'fg_color':"white"} 

TRIGGER_BUTTON_PLACE_COOR = {'x':206, 'y':60} 

TRIGGER_BUTTON_TEXT = "Generate"





