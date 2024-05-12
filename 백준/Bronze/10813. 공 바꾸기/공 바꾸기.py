def ball_count() :
    str_bucket_count, str_ball_cycle = input().split()              # 5, 4

    bucket_count = int(str_bucket_count)
    ball_cycle = int(str_ball_cycle)

    ball_count = []

    for x in range(1,bucket_count+1):                                       # 5번
        ball_count.append(x)
        pass


    for y in range(ball_cycle) :                                            # 4회
        str_bucket_first, str_bucket_second = input().split()
        bucket_first = int(str_bucket_first)-1
        bucket_second = int(str_bucket_second)-1

        
        bucket_refirst =  ball_count[bucket_first]
        ball_count[bucket_first] = ball_count[bucket_second]
        ball_count[bucket_second] = bucket_refirst
        pass
    ball_count = " ".join(map(str,ball_count))
    print(ball_count)

    return
ball_count()