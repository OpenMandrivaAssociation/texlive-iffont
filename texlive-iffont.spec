Name:		texlive-iffont
Version:	38823
Release:	2
Summary:	Conditionally load fonts with fontspec
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/iffont
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iffont.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iffont.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/iffont.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a macro to select the first font XeLaTeX
or LuaTeX can find in a comma separated list and, additionally,
a number of macro tests.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/iffont
%{_texmfdistdir}/tex/latex/iffont
%doc %{_texmfdistdir}/doc/latex/iffont

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
