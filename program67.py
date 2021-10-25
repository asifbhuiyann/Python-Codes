class phone() :
    def call(self):
        print("You can call.")

    def message(self):
        print("You can message.")

class samsung(phone) :
    def photo(self):
        print("You can take photo.")

    def video(self):
        print("You can record video.")

p = phone()
p.call()
p.message()

s = samsung()
s.photo()
s.video()
s.call()
s.message()
