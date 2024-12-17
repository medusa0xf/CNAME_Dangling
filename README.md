![](https://images.squarespace-cdn.com/content/v1/5bd6645551f4d49caf7eef4b/1582595851511-0KBNCM3DUN2SDJ9RM787/2-GradientSMALL.gif?format=1500w)
# CNAME_Dangling
This tool automates the process of checking for CNAME dangling issues by verifying if a CNAME record points to a valid, resolvable domain. It helps identify broken or misconfigured CNAME records that could lead to security vulnerabilities.

Run this command to install the dnspython library before running the tool

```bash
pip install dnspython
```

Run the help command
```
python3 cname_dangling.py -h
```

![](https://github.com/medusa0xf/CNAME_Dangling/blob/master/help.png)

This is what the result will look like!

![](https://github.com/medusa0xf/CNAME_Dangling/blob/master/issue.png)




