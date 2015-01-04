
from gi.repository import GdkPixbuf, Gdk


class Helpers():
    interp_type = GdkPixbuf.InterpType.BILINEAR

    screen = Gdk.Screen().get_default()

    screen_width = screen.get_width()*.7
    screen_height = screen.get_height()*.7
    
    preview_width = 250
    preview_height = 500
    
    zoom_percent = 0.1


    @staticmethod
    def scale_pixbuf(pixbuf, width, height):
        return pixbuf.scale_simple(width, height, Helpers.interp_type)


    @staticmethod
    def scale_fit_screen(pixbuf):
        height = pixbuf.get_height()
        width = pixbuf.get_width()
        if width > Helpers.screen_width or height > Helpers.screen_height:
            scale = min(float(Helpers.screen_width)/width, float(Helpers.screen_height)/height)
            pixbuf = Helpers.scale_pixbuf(pixbuf, int(width*scale), int(height*scale))
        return pixbuf


    @staticmethod
    def scale_fit_window(window, pixbuf):
        win_width, win_height = window.get_size()
        win_height -= 201
        win_width -= 158
        img_width, img_height = (pixbuf.get_width(), pixbuf.get_height())
        width_scale, height_scale = (win_width/float(img_width), win_height/float(img_height))
        if win_width != img_width and win_height != img_height:
            if width_scale < height_scale:
                win_height = int(img_height*width_scale) 
            else:
                win_width = int(img_width*height_scale)
            return Helpers.scale_pixbuf(window.pixbuf, win_width, win_height)
        else:
            if win_width == img_width and win_height < img_height:
                win_width = int(img_width*height_scale)
                return Helpers.scale_pixbuf(window.pixbuf, win_width, win_height)
            elif win_height == img_height and win_width < img_width:
                win_height = int(img_height*width_scale)
                return Helpers.scale_pixbuf(window.pixbuf, win_width, win_height)
        return pixbuf


    @staticmethod
    def make_preview(pixbuf):
        width = pixbuf.get_width()
        height = pixbuf.get_height()
        if width > Helpers.preview_width or height > Helpers.preview_height:
            scale = min(float(Helpers.preview_width)/width, float(Helpers.preview_height)/height)
            pixbuf = Helpers.scale_pixbuf(pixbuf, int(width*scale), int(height*scale))
        return pixbuf


    @staticmethod
    def rotate_left(pixbuf):
        return pixbuf.rotate_simple(GdkPixbuf.PixbufRotation.COUNTERCLOCKWISE)
    

    @staticmethod
    def rotate_right(pixbuf):
        return pixbuf.rotate_simple(GdkPixbuf.PixbufRotation.CLOCKWISE)


    @staticmethod
    def zoom_in(pixbuf, width, height):
        scale = float(height)/pixbuf.get_height()
        new_width = int(pixbuf.get_width()*scale*(1 + Helpers.zoom_percent))
        new_height = int(pixbuf.get_height()*scale*(1 + Helpers.zoom_percent))
        return Helpers.scale_pixbuf(pixbuf, new_width, new_height)


    @staticmethod
    def zoom_out(pixbuf, width, height):
        scale = float(height)/pixbuf.get_height()
        new_width = int(pixbuf.get_width()*scale*(1 - Helpers.zoom_percent))
        new_height = int(pixbuf.get_height()*scale*(1 - Helpers.zoom_percent))
        return Helpers.scale_pixbuf(pixbuf, new_width, new_height)


