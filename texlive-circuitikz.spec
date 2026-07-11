%global tl_name circuitikz
%global tl_revision 79172

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8.6
Release:	%{tl_revision}.1
Summary:	Draw electrical networks with TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/circuitikz
License:	lppl gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/circuitikz.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/circuitikz.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a set of macros for naturally typesetting
electrical and (somewhat less naturally, perhaps) electronic networks.
It is designed as a tool that is easy to use, with a lean syntax, native
to LaTeX, and directly supporting PDF output format. It has therefore
been based on the very impressive PGF/TikZ package.

