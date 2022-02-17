import mammoth
from typing import Union

DocxTohtlm = "E:/_Projects/ClassRoomTools/app/templates/public/html1.html"

class convert:
    def __init__(self,InputFilePath : str,OutPutFilePath : str, result = False) -> Union[None,str] :
        
        try:
            with open(InputFilePath, "rb") as docx_file:
                result = mammoth.convert_to_html(docx_file)
                html = result.value # The generated HTML

            with open(OutPutFilePath, "w", encoding="utf-8") as f:
                f.write(html)
            f.close()
        except:
            if(result == True):
                print("file not created")
                
#convert("E:/_Projects/ClassRoomTools/test/hello.docx",DocxTohtlm)