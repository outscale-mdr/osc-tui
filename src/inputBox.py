import npyscreen.fmPopup
import npyscreen.wgmultiline
import npyscreen.fmPopup
import curses
import textwrap

class ConfirmCancelPopup(npyscreen.fmPopup.ActionPopup):
    def on_ok(self):
        self.value = True
    def on_cancel(self):
        self.value = False


def readString(default_value="Input Text", title="Message", form_color='STANDOUT'):

    F = ConfirmCancelPopup(name=title, color=form_color)
    F.preserve_selected_widget = True
    tf = F.add(npyscreen.Textfield)
    tf.width = tf.width - 1
    tf.value = default_value
    F.edit()
    if F.value is True:
        return tf.value
    else:
        return None

def readAKSK(title="Please type your AKSK", form_color='STANDOUT'):
    while True:
        F = ConfirmCancelPopup(name=title, color=form_color)
        F.preserve_selected_widget = True
        name = F.add(npyscreen.TitleText, name = "NAME:")
        ak = F.add(npyscreen.TitleText, name = "ACCESS KEY:")
        sk = F.add(npyscreen.TitleText, name = "SECRET KEY:")
        region = F.add_widget(
            npyscreen.TitleCombo,
            name="REGION:",
            values="eu-west-2 eu-west-1".split(),
            value=0,
            )
        #ak.width = ak.width - 1
        F.edit()
        if F.value is True:
            if name.value != '' and ak.value != '' and sk.value != '':
                return {name.value : {
                    'access_key' : ak.value,
                    'secret-key' : sk.value,
                    'region' : region.values[region.value]
                    }}
            else:
                npyscreen.notify_confirm("Please check that you filled all fields.","ERROR")
        else:
            return None