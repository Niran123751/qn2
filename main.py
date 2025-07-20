from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import io

app = FastAPI()

@app.post("/captcha")
async def solve_captcha(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))

    # OCR to extract text
    text = pytesseract.image_to_string(image)

    # Extract numbers and multiply
    import re
    nums = list(map(int, re.findall(r"\d{8}", text)))
    if len(nums) == 2:
        result = nums[0] * nums[1]
    else:
        return JSONResponse(content={"error": "Could not detect two 8-digit numbers."}, status_code=400)

    return {"answer": result, "email": "24f2005647@ds.study.iitm.ac.in"}
