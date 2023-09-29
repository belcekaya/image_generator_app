# Libraries for building GUI (Graphical User Interface)
import tkinter as tk
import customtkinter as ctk 

# Machine Learning libraries 
import torch
from torch import autocast
from diffusers import StableDiffusionPipeline

# Libraries for processing image 
from PIL import ImageTk

# private modules 
from authtoken import auth_token
import config as cf

# Create app user interface
app = tk.Tk()
app.geometry(cf.APP_GEOMETRY)
app.title(cf.APP_TITLE)
app.configure(bg=cf.APP_BACKGROUND)
ctk.set_appearance_mode(cf.APP_APPERANCE_MODE) 

# Create input box on the user interface 
prompt = ctk.CTkEntry(**cf.PROMPT_BOX_INTERFACE) 
prompt.place(**cf.PROMPT_BOX_PLACE_COOR)

# Create a placeholder to show the generated image
img_placeholder = ctk.CTkLabel(**cf.IMAGE_PLACEHOLDER_INTERFACE)
img_placeholder.place(cf.IMAGE_PLACEHOLDER_COOR)

# Download stable diffusion model from hugging face 
stable_diffusion_model = StableDiffusionPipeline.from_pretrained(cf.MODELID, revision=cf.REVISION, torch_dtype=torch.float16, use_auth_token=auth_token) 
stable_diffusion_model.to(cf.DEVICE) 

# Generate image from text 
def generate_image(): 
    """ This function generate image from a text with stable diffusion"""
    with autocast(cf.DEVICE): 
        image = stable_diffusion_model(prompt.get(),guidance_scale=cf.GUIDANCE_SCALE)["sample"][0]
    
    # Convert image values to uint8
    image_np = (image * 255).round().astype("uint8")
    
    # Save the generated image
    image_pil = ImageTk.fromarray(image_np)
    image_pil.save('generatedimage.png')
    
    # Display the generated image on the user interface
    img = ImageTk.PhotoImage(image_pil)
    img_placeholder.configure(image=img) 

# Create a trigger button to give the generate image action in the app.
trigger = ctk.CTkButton(**cf.TRIGGER_BUTTON_INTERFACE, command=generate_image) 
trigger.configure(text=cf.TRIGGER_BUTTON_TEXT)
trigger.place(**cf.TRIGGER_BUTTON_PLACE_COOR) 

app.mainloop()