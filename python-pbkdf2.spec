Name:		python-pbkdf2
Version:	1.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pbkdf2/pbkdf2-%{version}.tar.gz
Summary:	PKCS#5 v2.0 PBKDF2 Module
URL:		https://pypi.org/project/pbkdf2/
License:	UNKNOWN
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
PKCS#5 v2.0 PBKDF2 Module

%files
%{py_sitedir}/pbkdf2.py
%{py_sitedir}/pbkdf2-*.*-info
