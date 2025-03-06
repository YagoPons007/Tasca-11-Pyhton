def concatenar():
   llista1 = ["sub", "supra"]
   llista2 = ["campió", "campiona"]
   connector = "-"


   return [f"{a}{connector}{b}" for a, b in zip(llista1, llista2)]


print(concatenar())
