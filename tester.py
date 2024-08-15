from langstring import LangString, GlobalFlag, Controller, LangStringFlag

Controller.set_flag(LangStringFlag.STRIP_LANG, True)

ls1 = LangString("teste","EN")
ls2 = LangString("teste","en ")

print(ls1==ls2)

