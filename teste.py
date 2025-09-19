import pandas as pd

# 1. Carregar a planilha original
df = pd.read_csv("EXP_2021_MUN.csv", sep=";")

# 2. Filtrar apenas as linhas onde SG_UF_MUN == "SP"
df_sp = df[df["SG_UF_MUN"] == "SP"]

# 3. (opcional) Mostrar quantas linhas foram mantidas e removidas
print("Total original:", len(df))
print("Total SP:", len(df_sp))
print("Removidas:", len(df) - len(df_sp))

# 4. Salvar em um novo arquivo CSV
df_sp.to_csv("EXP_2021_MUN_SP.csv", sep=";", index=False)

print("Arquivo filtrado salvo como EXP_2021_MUN_SP.csv")
