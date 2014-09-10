class CKEditorSettings(object):
    CKEDITOR_UPLOAD_PATH = 'uploads/'
    CKEDITOR_CONFIGS = {
        'default': {
            'toolbar': [
                ['Undo', 'Redo',
                 '-', 'Format',
                 '-', 'Bold', 'Italic', 'Underline',
                 '-', 'Link', 'Unlink',
                 '-', 'BulletedList', 'NumberedList',
                ],
                [
                    'SpellChecker', 'Scayt',
                ],
                [
                    '-', 'PasteText', 'PasteFromWord',
                    '-', 'Source',
                ]
            ],
            # 'height': 300,
            'width': 554,
        },
    }