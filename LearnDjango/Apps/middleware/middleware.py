def my_middleware(get_response):
    print('Initialized')
    def my_function(request):
        print('This is Before View')
        response = get_response(request)
        print('This is After View')
        return response
    return my_function