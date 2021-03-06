Name: opa-mpi-apps
Version: 10.4.0.0
Release: 92%{?dist}
Summary: Intel MPI benchmarks and Applications used by opa-fast-fabric
Group: System Environment/Libraries
License: GPLv2/BSD
Url: http://www.intel.com/
Source: opa-mpi-apps.tgz

AutoReq: no

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Contains applications and source for testing MPI performance in conjunction with opa-fastfabric or stand alone.


%prep
%setup -q -c


%build



%install

%define mpi_apps_files bandwidth latency osu2 hpl-2.0 imb PMB2.2.1 osu-micro-benchmarks-3.8-July12 mpi_multibw


mkdir -p $RPM_BUILD_ROOT/usr/lib/opa/src/mpi_apps

cd ./MpiApps
cp ./apps/* -r $RPM_BUILD_ROOT/usr/lib/opa/src/mpi_apps/

echo "/usr/lib/opa/src/mpi_apps/%{mpi_apps_files}" > %{_builddir}/mpi_apps.list
sed -i 's;[ ];\n/usr/lib/opa/src/mpi_apps/;g' %{_builddir}/mpi_apps.list 


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{_builddir}/mpi_apps.list

%changelog
* Wed Dec 2 2015 Brandon Yates <brandon.yates@intel.com>
- Initial Creation


