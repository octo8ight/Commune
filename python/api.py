from solana.keypair import Keypair
from solana.rpc.api import Client
from solana.rpc.commitment import Confirmed
from solana.rpc.types import TxOpts
from spl.token.instructions import TransferCheckedParams, transfer_checked, mint_to_checked, MintToCheckedParams, burn_checked, BurnCheckedParams, create_associated_token_account
from solana.transaction import Transaction

SECRET_KEY = bytes([88,150,17,189,65,143,176,126,52,12,61,23,168,139,252,168,59,142,5,149,126,107,199,238,85,70,15,3,209,1,251,27,199,178,19,146,128,103,141,145,146,110,198,58,91,47,242,255,115,30,251,34,189,117,190,119,49,134,31,15,3,110,19,221])

def mint(endpoint, program_id, dest, mint_account, mint_authority, amount, decimals, signers):
    transaction = Transaction()
    transaction.add(
        mint_to_checked(
            MintToCheckedParams(
                program_id=program_id,
                mint=mint_account,
                dest=dest,
                mint_authority=mint_authority,
                amount=amount,
                decimals=decimals,
                signers=signers
            )
        )
    )
    client = Client(endpoint=endpoint, commitment=Confirmed)
    client.send_transaction(transaction, Keypair.from_secret_key(SECRET_KEY), opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))

def burn(endpoint, program_id, mint_account, account, owner, amount, decimals, signers):
    transaction = Transaction()
    transaction.add(
        burn_checked(
            BurnCheckedParams(
                program_id=program_id,
                mint=mint_account,
                account=account,
                owner=owner,
                amount=amount,
                decimals=decimals,
                signers=signers
            )
        )
    )
    client = Client(endpoint=endpoint, commitment=Confirmed)
    client.send_transaction(transaction, Keypair.from_secret_key(SECRET_KEY), opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))

def transfer(endpoint, program_id, source, mint_account, dest, owner, amount, decimals, signers):
    transaction = Transaction()
    transaction.add(
        transfer_checked(
            TransferCheckedParams(
                program_id=program_id,
                source=source,
                mint=mint_account,
                dest=dest,
                owner=owner,
                amount=amount,
                decimals=decimals,
                signers=signers
            )
        )
    )
    client = Client(endpoint=endpoint, commitment=Confirmed)
    client.send_transaction(transaction, Keypair.from_secret_key(SECRET_KEY), opts=TxOpts(skip_confirmation=False, preflight_commitment=Confirmed))