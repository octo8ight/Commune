from solana.publickey import PublicKey
from spl.token.constants import TOKEN_PROGRAM_ID
from api import mint, burn, transfer

endPoint = "https://api.devnet.solana.com"

SECRET_KEY = bytes([88,150,17,189,65,143,176,126,52,12,61,23,168,139,252,168,59,142,5,149,126,107,199,238,85,70,15,3,209,1,251,27,199,178,19,146,128,103,141,145,146,110,198,58,91,47,242,255,115,30,251,34,189,117,190,119,49,134,31,15,3,110,19,221])
authority_Account = PublicKey("ESXdAhdrFwGxd9ytp4cYQtj7FXFcRNXSX9QzhJrqizCL")
token_Account = PublicKey("8Bh1oWfPqkvc7twEeMp61V9KJ9aBBcvjuwTM71R3TxTb")
to_Account = PublicKey("2pCVEugQ3Kdme9Pi9PcyBAB4E249sPWjocBdq55fJnMN")
token_Address = PublicKey("Fi8Q7AV8Nr8fJy27j4QpnHe3iJCHHsPcYQ1TSUoi8A1J")

def main():

    mint(
        endpoint=endPoint,
        program_id=TOKEN_PROGRAM_ID,
        dest=token_Account,
        mint_account=token_Address,
        mint_authority=authority_Account,
        amount=100000000000,
        decimals=9,
        signers=[]
    )

    burn(
        endpoint=endPoint,
        program_id=TOKEN_PROGRAM_ID,
        mint_account=token_Address,
        account=token_Account,
        owner=authority_Account,
        amount=100000000000,
        decimals=9,
        signers=[]
    )

    transfer(
        endpoint=endPoint,
        program_id=TOKEN_PROGRAM_ID,
        source=token_Account,
        mint_account=token_Address,
        dest=to_Account,
        owner=authority_Account,
        amount=100000000000,
        decimals=9,
        signers=[]
    )

main()