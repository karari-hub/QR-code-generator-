import qrcode 



class Qr_code:
    
    def __init__(self):
        pass


    def prompt_input(self, prompt):
        self.prompt = prompt
        prompt=input('prompt > ')
        return prompt
    
    def file_name(self, filename):
        self.filename = filename
        filename = input('file_name > ')
        return filename
        
        
    def qrcode_generator (self, prompt ,  filename ): 
        qr = qrcode.QRCode(
            version= 1, 
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=5,
            )
        qr.add_data(prompt)
        qr.make(fit=True)

        img = qr.make_image(fill_color = "black", back_color='white')
        img.save(filename)
        return

qr= Qr_code()

