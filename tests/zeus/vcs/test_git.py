        shell=True
    )
        shell=True
    )
        shell=True
    )
        shell=True
    )
        'cd %s && touch BAZ && git add BAZ && git commit -m "bazzy"' % remote_path, shell=True
    )
        shell=True
    )
        shell=True
    )
        revision, author='Foo Bar <foo@example.com>', message='biz\nbaz\n', subject='biz'
    )
        child_in_question=revisions[0].id, parent_in_question=revisions[1].id
    )
        child_in_question=revisions[1].id, parent_in_question=revisions[0].id
    ) is False