%global tl_name chemfig
%global tl_revision 78296

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.71
Release:	%{tl_revision}.1
Summary:	Draw molecules with easy syntax
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/chemfig
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chemfig.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(simplekv)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the command \chemfig{<code>}, which draws molecules
using the TikZ package. The <code> argument provides instructions for
the drawing operation. While the diagrams produced are essentially
2-dimensional, the package supports many of the conventional notations
for illustrating the 3-dimensional layout of a molecule. The package
uses TikZ for its actual drawing operations.

