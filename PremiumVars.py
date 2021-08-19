from pydantic import BaseModel

class PremiumVars(BaseModel): 
      Age : int
      Diabetes : int 
      BloodPressureProblems : int 
      AnyTransplants : int 
      AnyChronicDiseases: int 
      Height: int 
      Weight : int 
      KnownAllergies : int 
      HistoryOfCancerInFamily: int 
      NumberOfMajorSurgeries: int 