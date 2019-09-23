import nfc


def startup(targets):
    print("> waiting for new NFC tags...")
    return targets


def connected(tag):
    print("> connected!")
    if not tag.ndef or not tag.ndef.is_writeable:
        print("> not a writeable nfc tag")
        return False
    if tag.ndef.length > 0:
        print("Current NDEF Message:")
        for i, record in enumerate(tag.ndef.records):
            print("record", i + 1)
            print("  type =", repr(record.type))
            print("  name =", repr(record.name))
            print("  data =", repr(record.data))
    return True


def released(tag):
    print("> released!")


if __name__ == '__main__':
    clf = nfc.ContactlessFrontend('usb')
    print(clf)
    if clf:
        while clf.connect(rdwr={
            'on-startup': startup,
            'on-connect': connected,
            'on-release': released,
        }):
            pass
