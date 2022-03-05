#include "bbs.hpp"
#include <stdio.h>

int main() {
  ExternError *err = new ExternError();
  uint64_t handle = bbs_sign_context_init(err);
  printf("errorcode: %i\n", err->code);
  ExternError *erro = new ExternError();
  bbs_sign_context_add_message_string(handle, "Hello World", erro);
  printf("response code: %i\n", erro->code);
  printf("response msg: %s\n", erro->message);
  return 1;
}
