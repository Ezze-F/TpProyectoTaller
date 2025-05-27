$(document).ready(function() {
    $('#tabla').DataTable({
        "language": {
            "url": "//cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json",
            "decimal": "",
            "emptyTable": "No hay datos disponibles en la tabla",
            "info": "Mostrando _START_ a _END_ de _TOTAL_ registros",
            "infoEmpty": "Mostrando 0 a 0 de 0 registros",
            "infoFiltered": "(filtrado de _MAX_ registros totales)",
            "lengthMenu": "Mostrar _MENU_ registros",
            "loadingRecords": "Cargando...",
            "processing": "Procesando...",
            "search": "Buscar",
            "zeroRecords": "No se encontraron resultados",
            "paginate": {
                "first": "Primero",
                "last": "Último",
                "next": "Siguiente",
                "previous": "Anterior"
            },
            "aria": {
                "sortAscending": ": activar para ordenar ascendente",
                "sortDescending": ": activar para ordenar descendente"
            }
        },
        "responsive": true,
        "dom": '<"top"lf>rt<"bottom"ip><"clear">',
        "columnDefs": [
            { 
                "targets": [7], 
                "orderable": false,
                "searchable": false,
                "className": "dt-center" // Centra los botones
            }
        ]
    });
});