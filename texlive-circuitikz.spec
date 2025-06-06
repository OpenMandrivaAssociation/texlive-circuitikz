Name:		texlive-circuitikz
Version:	74723
Release:	1
Summary:	Draw electrical networks with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/circuitikz
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circuitikz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/circuitikz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a set of macros for naturally typesetting
electrical and (somewhat less naturally, perhaps) electronic
networks. It is designed as a tool that is easy to use, with a
lean syntax, native to LaTeX, and directly supporting PDF
output format. So is based on the very impressive pgf/TikZ
package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/circuitikz
%{_texmfdistdir}/tex/generic/circuitikz
%{_texmfdistdir}/tex/context/third/circuitikz
%doc %{_texmfdistdir}/doc/generic/circuitikz
%doc %{_texmfdistdir}/doc/latex/circuitikz
%doc %{_texmfdistdir}/doc/context/third/circuitikz

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
