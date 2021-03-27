import sys
from os import TMP_MAX
from typing import List, Type, Union

from src.api import sign, verify
from src.fast_forward_interface.ffi_util import encode_bytes
from src.models.CreateProofRequest import CreateProofRequest
from src.models.ProofMessage import ProofMessage, ProofMessageType
from src.models.keys import BlindedBlsKeyPair
from src.models.SignRequest import SignRequest
from src.models.VerifyRequest import VerifyRequest


from src.models.keys import BlsKeyPair


def print_block(title: str, data: Union[str, None] = None):

    title = title.title()  # capitalize
    title = f" {title} "
    title = "{:^1}".format(title)
    title = "{:-^40}".format(title)

    print(title)
    print(data)
    print()


def print_type(name: str, var):
    print(f"name: {name}, type: {type(var)}, value: {var}")


def trace(frame, event, arg):
    print("%s, %s:%d" % (event, frame.f_code.co_filename, frame.f_lineno))
    return trace


def print_table(headers: List[str], data: List[str]):
    if len(headers) != len(data):
        raise TypeError("Header and data size must be equal")

    num_of_cols = len(headers)
    max_chars = 0
    for i in range(num_of_cols):
        if len(headers[i]) > max_chars:
            max_chars = len(headers[i])
        if len(data[i]) > max_chars:
            max_chars = len(data[i])


def test_sign_verify_success():
    messages = ["hello", "world"]
    g2_signing_keys = BlsKeyPair.generate_g2()

    sign_request = SignRequest(g2_signing_keys, messages)
    signature = sign(sign_request)

    verify_request = VerifyRequest(
        BlsKeyPair(g2_signing_keys.public_key), signature, messages
    )

    verified = verify(verify_request)

    print_block("Messages to be signed", str(messages))
    print_block("Public signing key", g2_signing_keys.public_key)
    print_block("Private signing key", g2_signing_keys.secret_key)
    print_block("Signature", signature)

    print_block("Verified?", verified)


def test_sign_verify_fail():
    messages = ["hello", "world"]
    faulty_messages = ["ewa", "world"]

    g2_signing_keys = BlsKeyPair.generate_g2()

    sign_request = SignRequest(g2_signing_keys, messages)
    signature = sign(sign_request)

    verify_request = VerifyRequest(
        BlsKeyPair(g2_signing_keys.public_key), signature, faulty_messages
    )

    verified = verify(verify_request)

    print_block("Messages to be signed", str(messages))
    print_block("Public signing key", g2_signing_keys.public_key)
    print_block("Private signing key", g2_signing_keys.secret_key)
    print_block("Signature", signature)

    print_block("Verified?", verified)


if __name__ == "__main__":
    messages = [
        ProofMessage(ProofMessageType.HiddenProofSpecificBlinding, b"hello"),
        ProofMessage(ProofMessageType.HiddenProofSpecificBlinding, b"world"),
    ]
    create_proof_request = CreateProofRequest()
