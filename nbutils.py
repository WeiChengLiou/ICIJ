#!/usr/bin/env python
# -*- coding: utf-8 -*-

def rendermd(markdown_str):
    if hasattr(markdown_str, '__iter__'):
    markdown_str = u''.join(markdown_str)
    return HTML(u"<p>{}</p>".format(markdown(markdown_str)))

class ListTable(list):
    """ Overridden list class which takes a 2-dimensional list of 
    the form [[1,2,3],[4,5,6]], and renders an HTML Table in 
    IPython Notebook. """

    def _repr_html_(self):
        html = [u"<table>"]
        for row in self:
            html.append(u"<tr>")

            for col in row:
                html.append(u"<td>{0}</td>".format(unicode(col)))

            html.append(u"</tr>")
        html.append(u"</table>")
        return u''.join(html)

def table_attr(s, border=1):
    return s.replace(u'<table>',u'<table border="{0}">'.format(border))

def html_template(htmlstr,**kwargs):
    return u"""<!DOCTYPE: html>
        <meta charset="utf-8"><style>
        table {{
        border-collapse: collapse;
        }}
        td {{
        padding: 5px;
        }}
        table,th,td
        {{
        border:1px solid black;
        }}
        </style>
        <html>
        <body>
        {0}
        </body>
        </html>""".format(u''.join(map(unicode,htmlstr)))

def writehtml(li, fi):
    with open(fi, 'wb') as f:
        f.write(html_template(ListTable(li)._repr_html_()).encode('utf8'))

def writecsv(li, fi):
    with open(fi, 'wb') as csvfile:
        csvwriter = csv.writer(
            csvfile, delimiter=',',
            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for r in li:
            csvwriter.writerow(map(lambda x:unicode(x).encode('utf8'),r))

def htmlcsv(msg, df, fi):
    html_url = u"{0}/html/{1}.html".format(output_path, fi)
    csv_url = u"{0}/csv/{1}.csv".format(output_path, fi)
    writehtml(df, html_url)
    writecsv(df, csv_url)
    markdown_str=u"{0}：[HTML]({1}), [CSV]({2})".format(msg, html_url, csv_url)
    return HTML(u"{}</p>".format(markdown(markdown_str)))

def write_d3(fi, dir, **kwargs):
    """
    Export d3 file, return htmrul
    """
    fi1=fi.replace('json', 'html')
    htmlfi = os.path.join(output_path, dir, fi1)
    htmlurl = os.path.join(urlpath, dir, fi1)

    render_html(htmlfi, FileName=fi, **kwargs)
    return unicode(htmlurl)
