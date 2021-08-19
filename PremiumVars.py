from pydantic import BaseModel

class PremiumVars(BaseModel): 
      Age: float
      Diabetes: float 
      BloodPressureProblems: float 
      AnyTransplants: float 
      AnyChronicDiseases: float 
      Height: float 
      Weight: float 
      KnownAllergies: float  
      HistoryOfCancerInFamily: float  
      NumberOfMajorSurgeries: float  