import openai

openai.api_key = "your_openai_api_key"

def analyze_eth_vs_sol(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a serious crypto analyst specialized in Ethereum and Solana."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    while True:
        user_input = input("Ask about ETH vs SOL: ")
        print(analyze_eth_vs_sol(user_input))
