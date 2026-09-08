#!/usr/bin/env python3
"""
提词器App图标 v2 - 更精致的渐变设计
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                          "app", "src", "main", "res")
ICON_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                        "release", "icons")

ICON_SIZES = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192,
}

LAUNCHER_SIZES = {
    'mipmap-mdpi': 108,
    'mipmap-hdpi': 162,
    'mipmap-xhdpi': 216,
    'mipmap-xxhdpi': 324,
    'mipmap-xxxhdpi': 432,
}


def draw_gradient_rounded_rect(draw, bbox, radius, color_top, color_bottom):
    """绘制渐变圆角矩形"""
    x0, y0, x1, y1 = bbox
    for y in range(y0, y1):
        ratio = (y - y0) / max(1, (y1 - y0 - 1))
        r = int(color_top[0] + (color_bottom[0] - color_top[0]) * ratio)
        g = int(color_top[1] + (color_bottom[1] - color_top[1]) * ratio)
        b = int(color_top[2] + (color_bottom[2] - color_top[2]) * ratio)
        # 只在圆角区域外画线，圆角由 rounded_rectangle 处理
        draw.line([(x0, y), (x1 - 1, y)], fill=(r, g, b))
    # 用mask方式做圆角
    # 先画到临时图再用圆角mask
    pass


def create_icon(size=512):
    """生成提词器App图标 v2 - 渐变+立体"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    s = size / 512.0
    
    # === 背景：深蓝渐变圆角矩形 ===
    radius = int(100 * s)
    # 上色深蓝，下色更深
    color_top = (22, 33, 62)    # #16213E
    color_bottom = (15, 20, 40)  # #0F1428
    
    # 绘制渐变背景
    bg = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    bg_draw = ImageDraw.Draw(bg)
    for y in range(size):
        ratio = y / max(1, size - 1)
        r = int(color_top[0] + (color_bottom[0] - color_top[0]) * ratio)
        g = int(color_top[1] + (color_bottom[1] - color_top[1]) * ratio)
        b = int(color_top[2] + (color_bottom[2] - color_top[2]) * ratio)
        bg_draw.line([(0, y), (size - 1, y)], fill=(r, g, b, 255))
    
    # 圆角mask
    mask = Image.new('L', (size, size), 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.rounded_rectangle([0, 0, size-1, size-1], radius=radius, fill=255)
    
    img = Image.composite(bg, Image.new('RGBA', (size, size), (0, 0, 0, 0)), mask)
    draw = ImageDraw.Draw(img)
    
    # === 镜头圆圈 ===
    cx, cy = int(256 * s), int(215 * s)
    
    # 镜头外圈光晕
    for i in range(3):
        glow_r = int((135 + i * 8) * s)
        alpha = 30 - i * 10
        draw.ellipse([cx-glow_r, cy-glow_r, cx+glow_r, cy+glow_r], 
                     fill=(0, 180, 216, max(0, alpha)))
    
    # 镜头外圈
    outer_r = int(115 * s)
    draw.ellipse([cx-outer_r, cy-outer_r, cx+outer_r, cy+outer_r], 
                 fill=(15, 52, 96), outline=(0, 150, 200, 200), width=int(4*s))
    
    # 镜头内圈渐变效果
    inner_r = int(90 * s)
    # 内圈用渐变
    inner_img = Image.new('RGBA', (int(inner_r*2+2), int(inner_r*2+2)), (0, 0, 0, 0))
    inner_draw = ImageDraw.Draw(inner_img)
    for y_pos in range(int(inner_r*2+2)):
        ratio = y_pos / max(1, int(inner_r*2+1))
        r = int(8 + ratio * 4)
        g = int(12 + ratio * 8)
        b = int(30 + ratio * 15)
        inner_draw.line([(0, y_pos), (int(inner_r*2+1), y_pos)], fill=(r, g, b, 255))
    inner_mask = Image.new('L', (int(inner_r*2+2), int(inner_r*2+2)), 0)
    inner_mask_draw = ImageDraw.Draw(inner_mask)
    inner_mask_draw.ellipse([0, 0, int(inner_r*2+1), int(inner_r*2+1)], fill=255)
    inner_img = Image.composite(inner_img, Image.new('RGBA', inner_img.size, (0, 0, 0, 0)), inner_mask)
    img.paste(inner_img, (cx-inner_r, cy-inner_r), inner_img)
    draw = ImageDraw.Draw(img)
    
    # 镜头内部深色
    lens_r = int(65 * s)
    draw.ellipse([cx-lens_r, cy-lens_r, cx+lens_r, cy+lens_r], 
                 fill=(5, 8, 20))
    
    # 镜头内部反光弧
    lens2_r = int(55 * s)
    draw.ellipse([cx-lens2_r, cy-lens2_r, cx+lens2_r, cy+lens2_r], 
                 fill=(15, 25, 55))
    
    # 高光点
    hl_r = int(22 * s)
    hl_x, hl_y = cx - int(22 * s), cy - int(22 * s)
    draw.ellipse([hl_x-hl_r, hl_y-hl_r, hl_x+hl_r, hl_y+hl_r], 
                 fill=(100, 210, 240, 200))
    # 小高光点
    hl2_r = int(8 * s)
    draw.ellipse([hl_x+int(18*s)-hl2_r, hl_y+int(25*s)-hl2_r, 
                   hl_x+int(18*s)+hl2_r, hl_y+int(25*s)+hl2_r], 
                 fill=(150, 220, 240, 120))
    
    # === 录制指示灯 ===
    dot_x, dot_y = int(380 * s), int(128 * s)
    dot_r = int(16 * s)
    # 红点光晕
    draw.ellipse([dot_x-dot_r-int(8*s), dot_y-dot_r-int(8*s), 
                   dot_x+dot_r+int(8*s), dot_y+dot_r+int(8*s)], 
                 fill=(255, 59, 48, 40))
    draw.ellipse([dot_x-dot_r, dot_y-dot_r, dot_x+dot_r, dot_y+dot_r], 
                 fill=(255, 59, 48))
    # 红点高光
    draw.ellipse([dot_x-int(5*s), dot_y-int(6*s), 
                   dot_x+int(2*s), dot_y-int(1*s)], 
                 fill=(255, 160, 150, 180))
    
    # === 提词文字线条 ===
    accent = (0, 200, 230)  # #00C8E6 亮青色
    
    line_y_start = int(365 * s)
    line_height = int(26 * s)
    line_left = int(130 * s)
    line_right = int(382 * s)
    line_right_short = int(300 * s)
    
    for i in range(3):
        y = line_y_start + i * line_height
        r_line = line_right if i != 2 else line_right_short
        alpha = 240 if i == 0 else (180 if i == 1 else 120)
        h = int(14 * s)
        
        # 线条渐变（左亮右暗）
        for x in range(int(line_left), int(r_line)):
            ratio = (x - line_left) / max(1, r_line - line_left)
            r = int(accent[0] * (1 - ratio * 0.3))
            g = int(accent[1] * (1 - ratio * 0.3))
            b = int(accent[2] * (1 - ratio * 0.2))
            draw.line([(x, y), (x, y + h)], fill=(r, g, b, alpha))
        
        # 线条圆角覆盖（简化：用圆角矩形重新画）
        # 不逐像素了，用圆角矩形
        bar_img = Image.new('RGBA', (int(r_line - line_left), h + int(4*s)), (0, 0, 0, 0))
        bar_draw = ImageDraw.Draw(bar_img)
        bar_draw.rounded_rectangle([0, 0, int(r_line - line_left)-1, h-1], 
                                    radius=int(7*s), fill=(accent[0], accent[1], accent[2], alpha))
        img.paste(bar_img, (int(line_left), int(y)), bar_img)
    
    draw = ImageDraw.Draw(img)
    
    return img


def create_adaptive_icon_foreground(size=432):
    """自适应图标前景"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    s = size / 432.0
    
    cx, cy = int(216 * s), int(175 * s)
    outer_r = int(100 * s)
    inner_r = int(78 * s)
    lens_r = int(55 * s)
    
    highlight_color = (0, 200, 230)
    accent_color = (15, 52, 96)
    
    # 光晕
    for i in range(3):
        glow_r = int((115 + i * 7) * s)
        alpha = 25 - i * 8
        draw.ellipse([cx-glow_r, cy-glow_r, cx+glow_r, cy+glow_r], 
                     fill=(highlight_color[0], highlight_color[1], highlight_color[2], max(0, alpha)))
    
    draw.ellipse([cx-outer_r, cy-outer_r, cx+outer_r, cy+outer_r], 
                 fill=accent_color, outline=(highlight_color[0], highlight_color[1], highlight_color[2], 180), width=int(3*s))
    draw.ellipse([cx-inner_r, cy-inner_r, cx+inner_r, cy+inner_r], 
                 fill=(8, 12, 25))
    draw.ellipse([cx-lens_r, cy-lens_r, cx+lens_r, cy+lens_r], 
                 fill=(15, 25, 50))
    
    # 高光
    hl_r = int(18 * s)
    hl_x, hl_y = cx - int(18*s), cy - int(18*s)
    draw.ellipse([hl_x-hl_r, hl_y-hl_r, hl_x+hl_r, hl_y+hl_r], 
                 fill=(highlight_color[0], highlight_color[1], highlight_color[2], 200))
    
    # 文字线条
    line_y_start = int(300 * s)
    line_height = int(22 * s)
    line_left = int(108 * s)
    line_right = int(324 * s)
    line_right_short = int(256 * s)
    
    for i in range(3):
        y = line_y_start + i * line_height
        r_line = line_right if i != 2 else line_right_short
        alpha = 220 if i == 0 else (160 if i == 1 else 100)
        h = int(12 * s)
        bar_img = Image.new('RGBA', (int(r_line - line_left), h + int(4*s)), (0, 0, 0, 0))
        bar_draw = ImageDraw.Draw(bar_img)
        bar_draw.rounded_rectangle([0, 0, int(r_line - line_left)-1, h-1], 
                                    radius=int(6*s), 
                                    fill=(highlight_color[0], highlight_color[1], highlight_color[2], alpha))
        img.paste(bar_img, (int(line_left), int(y)), bar_img)
    
    # 红点
    dot_x, dot_y = int(315 * s), int(105 * s)
    dot_r = int(14 * s)
    draw = ImageDraw.Draw(img)
    draw.ellipse([dot_x-dot_r, dot_y-dot_r, dot_x+dot_r, dot_y+dot_r], 
                 fill=(255, 59, 48))
    draw.ellipse([dot_x-int(4*s), dot_y-int(5*s), dot_x+int(2*s), dot_y], 
                 fill=(255, 160, 150, 170))
    
    return img


def create_adaptive_icon_background(size=432):
    """自适应图标背景 - 深蓝渐变"""
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    color_top = (22, 33, 62)
    color_bottom = (15, 20, 40)
    
    for y in range(size):
        ratio = y / max(1, size - 1)
        r = int(color_top[0] + (color_bottom[0] - color_top[0]) * ratio)
        g = int(color_top[1] + (color_bottom[1] - color_top[1]) * ratio)
        b = int(color_top[2] + (color_bottom[2] - color_top[2]) * ratio)
        draw.line([(0, y), (size - 1, y)], fill=(r, g, b, 255))
    
    return img


def main():
    os.makedirs(ICON_DIR, exist_ok=True)
    
    # 512x512 商店图标
    print("生成 512x512 商店图标...")
    icon_512 = create_icon(512)
    icon_512.save(os.path.join(ICON_DIR, "icon_512.png"), "PNG")
    icon_512.save(os.path.join(ICON_DIR, "ic_launcher_web_512.png"), "PNG")
    
    # 各尺寸mipmap图标
    for folder, size in ICON_SIZES.items():
        print(f"生成 {folder}/ic_launcher ({size}x{size})...")
        out_dir = os.path.join(OUTPUT_DIR, folder)
        os.makedirs(out_dir, exist_ok=True)
        icon = create_icon(size)
        icon.save(os.path.join(out_dir, "ic_launcher.png"), "PNG")
    
    # 自适应图标前景和背景
    for folder, size in LAUNCHER_SIZES.items():
        print(f"生成 {folder}/ic_launcher_foreground ({size}x{size})...")
        out_dir = os.path.join(OUTPUT_DIR, folder)
        os.makedirs(out_dir, exist_ok=True)
        fg = create_adaptive_icon_foreground(size)
        fg.save(os.path.join(out_dir, "ic_launcher_foreground.png"), "PNG")
        
        bg = create_adaptive_icon_background(size)
        bg.save(os.path.join(out_dir, "ic_launcher_background.png"), "PNG")
    
    print(f"\n✅ 图标全部生成完成！")
    print(f"   商店图标: {os.path.join(ICON_DIR, 'icon_512.png')}")
    print(f"   mipmap目录: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()