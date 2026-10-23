import recap_ferme.cli as cli


def test_main(capsys):
    cli.main()
    captured = capsys.readouterr()
    assert captured.out == "CLI Project started...\n"
