"""
✅ SECURE IMPLEMENTATION ✅
Module: XSS Prevention - Output Encoding
"""
import html

def secure_render(user_input):
    """
    Securely escapes user input before rendering in HTML.
    """
    return html.escape(user_input)
