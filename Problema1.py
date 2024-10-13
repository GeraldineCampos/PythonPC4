import requests

def obtener_precio_bitcoin():
    # URL de la API de CoinDesk
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    try:
        respuesta = requests.get(url)
        
        respuesta.raise_for_status()
        datos = respuesta.json()  # Convertir la respuesta JSON en un diccionario
        return datos['bpi']['USD']['rate_float']  # Obtener el precio actual en USD
    
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
        return None

def calcular_valor_bitcoins(bitcoins, precio_bitcoin):
    # Calcular el valor total de los bitcoins
    valor_total = bitcoins * precio_bitcoin
    return valor_total

def main():
    try:
        # Solicitar al usuario la cantidad de bitcoins
        n = float(input("¿Cuántos bitcoins tienes?: "))
        
        # Obtener el precio actual de Bitcoin en USD
        precio_bitcoin_usd = obtener_precio_bitcoin()
        
        if precio_bitcoin_usd is not None:
            # Calcular el valor en USD de los bitcoins
            valor_total_usd = calcular_valor_bitcoins(n, precio_bitcoin_usd)
            
            # Mostrar el resultado con el formato adecuado
            print(f"El valor de {n} bitcoins es: ${valor_total_usd:,.4f}")
    
    except ValueError:
        # Manejo de errores en caso de que la entrada no sea un número válido
        print("Por favor, introduce un número válido de bitcoins.")

if __name__ == "__main__":
    main()