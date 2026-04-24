# === فیکسِ ارور torchvision ===
import sys
import torchvision.transforms.functional as TF
sys.modules['torchvision.transforms.functional_tensor'] = TF
# ==============================

import os
import cv2
import gradio as gr
from gfpgan import GFPGANer
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

# دانلود خودکار مدل‌ها (برای فرار از محدودیت حجم گیت‌هاب)
if not os.path.exists('GFPGANv1.3.pth'):
    print("Downloading GFPGAN model...")
    os.system('wget https://github.com/TencentARC/GFPGAN/releases/download/v1.3.0/GFPGANv1.3.pth')

if not os.path.exists('RealESRGAN_x2plus.pth'):
    print("Downloading RealESRGAN model...")
    os.system('wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.1/RealESRGAN_x2plus.pth')

# ۱. تنظیم مدل بک‌گراند
bg_model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=2)
bg_upsampler = RealESRGANer(
    scale=2,
    model_path='RealESRGAN_x2plus.pth',
    model=bg_model,
    tile=400,
    tile_pad=10,
    pre_pad=0,
    half=False) # روی سرورهای رایگان half باید False باشه

# ۲. روشن کردن مدل اصلی
restorer = GFPGANer(
    model_path='GFPGANv1.3.pth',
    upscale=2,
    arch='clean',
    channel_multiplier=2,
    bg_upsampler=bg_upsampler
)

# ۳. تابع پردازش
def magic_restore(img):
    try:
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cropped_faces, restored_faces, restored_img = restorer.enhance(
            img_bgr, has_aligned=False, only_center_face=False, paste_back=True)
        result = cv2.cvtColor(restored_img, cv2.COLOR_BGR2RGB)
        return result
    except Exception as e:
        return f"خطایی رخ داد: {str(e)}"

# ۴. رابط کاربری (Gradio)
interface = gr.Interface(
    fn=magic_restore,
    inputs=gr.Image(label="عکس داغون رو اینجا آپلود کن"),
    outputs=gr.Image(label="جادوی هوش مصنوعی"),
    title="🌟 ماشین زمان: ترمیم حرفه‌ای عکس",
    description="توسعه داده شده با Deep Learning. یک عکس قدیمی و بی‌کیفیت آپلود کنید و نتیجه را ببینید!"
)

interface.launch() # اینجا دیگه share=True نمی‌خوایم چون روی سرور اجرا میشه