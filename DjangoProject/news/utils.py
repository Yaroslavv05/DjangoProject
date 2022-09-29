class MyMixin(object):
    mixin_pro = ''

    def get_pro(self):
        return self.mixin_pro.upper()

    def get_upper(self, s):
        return s.upper
