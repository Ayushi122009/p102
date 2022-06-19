import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token= access_token
    
    def uploadfile(self, file_from, file_to):
        dbx= dropbox.Dropbox(self.access_token)
        f= open(file_from, "rb")
        dbx.files_upload(f.read(), file_to)
    
def main():
   access_token ="sl.BJGsljWWR9y_7ZBkEfJDB3hJbw2pIXHBn-d4LoLHdUdCLdWZWRqZjMwTIUPwJeBekSBYu_9VbPvdmUD8GNvaoIRtLhWU9bFvVI9ndooJHtiXWLQejrsADnJZ1njKyI2z3qXRbS6lYtE"
   transferdata = TransferData(access_token)
   
   file_from= input("Enter the file path to transfer: ")
   file_to= input("Enter the full path to upload to dropbox: ")

   transferdata.uploadfile(file_from, file_to)
   print("File has been moved!")

main()
