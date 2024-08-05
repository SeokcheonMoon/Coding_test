def bucket_counting() :
    bucket_count = [0]

    str_bucket_count, str_ball_cycle = input().split()      # 5 , 4
    bucket_count = int(str_bucket_count)*bucket_count

    ball_cycle = int(str_ball_cycle)

    for x in range(ball_cycle) :
        str_range_first,str_range_second,str_ball_number =input().split()

        range_first = int(str_range_first)
        range_second = int(str_range_second)
        ball_number = int(str_ball_number)
        pass


        for y in range(range_first,range_second+1):
            pass
            bucket_count[y-1] = ball_number
            pass
            
    only_count = ' '.join(map(str, bucket_count))
    print("{}".format(only_count))

    return 0

bucket_counting()