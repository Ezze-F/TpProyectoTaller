$(document).ready(function() {
    // Verifica y destruye inicializaciones anteriores
    if ($.fn.DataTable.isDataTable('#tabla_disponibles')) {
        $('#tabla_disponibles').DataTable().destroy();
    }
    if ($.fn.DataTable.isDataTable('#tabla_eliminados')) {
        $('#tabla_eliminados').DataTable().destroy();
    }

    // Inicializa tabla de disponibles ordenada descendentemente por "codigo"
    $('#tabla_disponibles').DataTable({
        language: {
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
            }
        },
        responsive: true,
        dom: '<"top"lf>rt<"bottom"ip><"clear">',
        order: [[0, 'desc']], // Columna 0 = código
        columnDefs: [
            {
                targets: [7], // columna "Acciones"
                orderable: false,
                searchable: false,
                className: "dt-center"
            }
        ]
    });

    // Inicializa tabla de eliminados, también puedes ordenar por código
    $('#tabla_eliminados').DataTable({
        language: {
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
            }
        },
        responsive: true,
        dom: '<"top"lf>rt<"bottom"ip><"clear">',
        order: [[0, 'desc']], // orden por código (columna 0)
        columnDefs: [
            {
                targets: [8], // columna "Acciones"
                orderable: false,
                searchable: false,
                className: "dt-center"
            }
        ]
    });
});