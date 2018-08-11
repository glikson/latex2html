import subprocess

def latex2html(event, context):
    latex = event["latex"]
    print "Latex:"
    print latex
    p = subprocess.Popen(args=["pandoc-2.2.3.2/bin/pandoc","--from=latex"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate(input=latex.encode('latin-1'))
    print out
    print err
    return {"html": out, "err": err}

