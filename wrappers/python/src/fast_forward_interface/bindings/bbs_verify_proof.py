from ctypes import POINTER, byref, c_char_p, c_ulong
import sys
from typing import Optional, Union
from src.fast_forward_interface import ExternError

from src.fast_forward_interface.ffi_util import (
    FfiByteBuffer,
    encode_bytes,
    encode_str,
    wrap_native_func,
)


if sys.version_info >= (3, 8):
    from typing import TypedDict  # pylint: disable=no-name-in-module
else:
    from typing_extensions import TypedDict


def bbs_verify_proof_context_init() -> int:
    func = wrap_native_func(
        "bbs_verify_proof_context_init", arg_types=[POINTER(ExternError)]
    )
    err = ExternError()
    handle = func(err)
    err.throw_on_error()
    return handle


def bbs_verify_proof_context_finish(handle: int) -> int:
    func = wrap_native_func(
        "bbs_verify_proof_context_finish", arg_types=[c_ulong, POINTER(ExternError)]
    )
    err = ExternError()
    result = func(handle, err)
    err.throw_on_error()
    return result


def bbs_verify_proof_context_add_message_string(handle: int, message: str) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_add_message_string",
        arg_types=[c_ulong, c_char_p, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_str(message), err)
    err.throw_on_error()


def bbs_verify_proof_context_add_message_bytes(handle: int, message: bytes) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_add_message_bytes",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_bytes(message), err)
    err.throw_on_error()


def bbs_verify_proof_context_add_message_prehashed(handle: int, message: bytes) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_add_message_prehashed",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_bytes(message), err)
    err.throw_on_error()


def bbs_verify_proof_context_set_proof(handle: int, proof: bytes) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_set_proof",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_bytes(proof), err)
    err.throw_on_error()


def bbs_verify_proof_context_set_public_key(handle: int, public_key: bytes) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_set_public_key",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_bytes(public_key), err)
    err.throw_on_error()


def bbs_verify_proof_context_set_nonce_string(handle: int, nonce: str) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_set_nonce_string",
        arg_types=[c_ulong, c_char_p, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_str(nonce), err)
    err.throw_on_error()


def bbs_verify_proof_context_set_nonce_bytes(handle: int, nonce: bytes) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_set_nonce_bytes",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_bytes(nonce), err)
    err.throw_on_error()


def bbs_verify_proof_context_set_nonce_prehashed(handle: int, nonce: bytes) -> None:
    func = wrap_native_func(
        "bbs_verify_proof_context_set_nonce_prehashed",
        arg_types=[c_ulong, FfiByteBuffer, POINTER(ExternError)],
    )
    err = ExternError()
    func(handle, encode_bytes(nonce), err)
    err.throw_on_error()


def bbs_get_total_messages_count_for_proof(proof: bytes) -> int:
    func = wrap_native_func(
        "bbs_get_total_messages_count_for_proof", arg_types=[FfiByteBuffer]
    )
    return func(encode_bytes(proof))
