

Installing the dependencies
"""

!pip install fastapi
!pip install uvicorn
!pip install pickle5
!pip install pydantic
!pip install scikit-learn
!pip install requests
!pip install pypi-json
!pip install pyngrok
!pip install nest-asyncio

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):

    PC1 : float
    PC2 : float
    PC3 : float
    PC4 : float
    PC5 : float
    PC6 : float
    PC7 : float
    PC8 : float
    PC9 : float
    PC10 : float
    PC11 : float
    PC12 : float
    PC13 : float
    PC14 : float
    PC15 : float
    PC16 : float
    PC17 : float
    PC18 : float
    PC19 : float
    PC20 : float
    PC21 : float
    PC22 : float
    PC23 : float
    PC24 : float
    PC25 : float
    PC26 : float
    PC27 : float
    PC28 : float
    PC29 : float
    PC30 : float
    PC31 : float
    PC32 : float
    PC33 : float
    PC34 : float
    PC35 : float
    PC36 : float
    PC37 : float
    PC38 : float
    PC39 : float
    PC40 : float
    PC41 : float
    PC42 : float
    PC43 : float
    PC44: float

# loading the saved model
Risk_model = pickle.load(open('final_best_model.sav', 'rb'))

@app.post('/risk_prediction')
def Risk_pred(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)




    input_list = [PC1,PC2,PC3,PC4,PC5,PC6,PC7,PC8,PC9,PC10,PC11,PC12,PC13,PC14,PC15,PC16,PC17,PC18,PC19,PC20,PC21,PC22,PC23,PC24,PC25,PC26,PC27,PC28,PC29,PC30,PC31,PC32,PC33,PC34,PC35,PC36,PC37,PC38,PC39,PC40,PC41,PC42,PC43,PC44]

    prediction = final_best_model.predict([input_list])

    if (prediction[0] == 0):
        return 'The status is not default'
    else:
        return 'The status is default'
