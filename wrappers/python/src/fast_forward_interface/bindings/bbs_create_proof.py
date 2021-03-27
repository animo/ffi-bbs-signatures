from ctypes import POINTER, byref, c_char_p, c_uint, c_ulong
import sys
from typing import Optional, Union
from src.fast_forward_interface.ExternError import ExternError

from src.fast_forward_interface.ffi_util import (
    FfiByteBuffer,
    encode_bytes,
    encode_str,
    wrap_native_func,
)
from src.models import ProofMessageType

if sys.version_info >= (3, 8):
    from typing import TypedDict  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict

# Binding functions
def bbs_create_proof_context_init() -> int:
    func = wrap_native_func(
        "bbs_create_proof_context_init",
        arg_types=[POINTER(ExternError)],
        return_type=c_ulong,
    )
    err = ExternError()
    handle = func(byref(err))
    err.throw_on_error()
    return handle


def bbs_create_proof_context_finish(
    handle: int,
) -> bytes:
    func = wrap_native_func(
        "bbs_create_proof_context_finish",
        arg_types=[c_ulong, POINTER(FfiByteBuffer), POINTER(ExternError)],
    )
    proof, err = FfiByteBuffer(), ExternError()
    func(handle, byref(proof), byref(err))
    err.throw_on_error
    return bytes(proof)


def bbs_create_proof_context_add_proof_message_string(
    handle: int,
    message: str,
    proof_message_type: ProofMessageType,
    blinding_factor: Optional[bytes] = None,
) -> None:
    # VERIFY the proof_message_type has to be passed as a c_uint (c_uint8 will probably be enough)
    func = wrap_native_func(
        "bbs_create_proof_context_add_proof_message_string",
        arg_types=[c_ulong, c_char_p, c_uint, FfiByteBuffer, POINTER(ExternError)],
    )

    err = ExternError()
    func(
        handle,
        encode_str(message),
        proof_message_type.value,
        encode_bytes(blinding_factor),
        byref(err),
    )
    err.throw_on_error()


def bbs_create_proof_context_add_proof_message_bytes(
    handle: int,
    message: FfiByteBuffer,
    proof_message_type: ProofMessageType,
    blinding_factor: FfiByteBuffer,
) -> None:
    # VERIFY the proof_message_type has to be passed as a c_uint (c_uint8 will probably be enough)
    func = wrap_native_func(
        "bbs_create_proof_context_add_proof_message_bytes",
        arg_types=[c_ulong, FfiByteBuffer, c_uint, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, message, proof_message_type.value, blinding_factor, byref(err))
    err.throw_on_error()


def bbs_create_proof_context_add_proof_message_prehashed(
    handle: int,
    message: FfiByteBuffer,
    proof_message_type: ProofMessageType,
    blinding_factor: FfiByteBuffer,
) -> None:
    # VERIFY the proof_message_type has to be passed as a c_uint (c_uint8 will probably be enough)
    func = wrap_native_func(
        "bbs_create_proof_context_add_proof_message_prehashed",
        arg_types=[c_ulong, FfiByteBuffer, c_uint, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, message, proof_message_type.value, blinding_factor, byref(err))
    err.throw_on_error()


def bbs_create_proof_context_set_signature(
    handle: int, signature: FfiByteBuffer
) -> None:
    func = wrap_native_func(
        "bbs_create_proof_context_set_signature",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, signature, byref(err))
    err.throw_on_error()


def bbs_create_proof_context_set_public_key(
    handle: int, public_key: FfiByteBuffer
) -> None:
    func = wrap_native_func(
        "bbs_create_proof_context_set_public_key",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, public_key, byref(err))
    err.throw_on_error()


def bbs_create_proof_context_set_nonce_string(handle: int, nonce: str) -> None:
    func = wrap_native_func(
        "bbs_create_proof_context_set_nonce_string",
        arg_types=[c_ulong, c_char_p, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_str(nonce), byref(err))
    err.throw_on_error()


def bbs_create_proof_context_set_nonce_bytes(handle: int, nonce: FfiByteBuffer) -> None:
    func = wrap_native_func(
        "bbs_create_proof_context_set_nonce_bytes",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, nonce, byref(err))
    err.throw_on_error()


def bbs_create_proof_context_set_nonce_prehashed(
    handle: int, nonce: FfiByteBuffer
) -> None:
    func = wrap_native_func(
        "bbs_create_proof_context_set_nonce_prehashed",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, nonce, byref(err))
    err.throw_on_error()