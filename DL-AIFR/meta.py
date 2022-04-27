mixture = {
    'train_root': '/data/fuzhuolin/cross_age/data/aligned_dlib_112x96/mixture/train',
    'val_root': '/data/fuzhuolin/cross_age/data/aligned_dlib_112x96/mixture/val',
    'pat': '_|\.',
    'pos': 1,
    'n_cls': 24652
}

FGNET = {
    'train_root': 'images',
    'val_root': None,
    'pat': 'A',
    'pos': 0,
    'n_cls': 82
}

vgg_toy = {
    'train_root': 'train',
    'val_root': 'val',
    'pat': '_|\. ',
    'pos': 1,
    'n_cls': 2000-19
}

age_cutoffs = [12, 18, 25, 35, 45, 55, 65]