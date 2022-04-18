## very Specific information

start = time.time()  # 시작 시간 저장

..(생략)...

parser.add_argument('--out-file', type=str, default="result.csv",
                    help='output file name(default : result.csv')
args = parser.parse_args()

if args.api_key is not None:
    API_LIST.append(args.api_key)

if args.api_list is not None:
    f_key = open(args.api_list, 'r')
    lines_key = f_key.readlines()
    for line in lines_key:
        API_LIST.append(line.strip())

        
print("- API key :",num_key)
print("- path :", args.list)



# create vt object list
vt = []
for val in API_LIST:
    vt.append(VTApi(val))


# check routine
results= []

key_order = 0

f = open(args.hash_list, 'r')
lines = f.readlines()
for val in lines:
    if key_order == num_key:
        key_order =0

    per_hash = val.strip()

    try:

        response = vt[key].get_file_report(hash)

        try:
            md5 = response['results']['md5']
        except:
            md5 = "-"

        try:
            sha256= response['results']['sha256']
        except:
            sha256 = "-"

        try:
            sha1= response['results']['sha1']
        except:
            sha1 = "-"
        ...(중간 생략)...


print("Run time :", time.time() - start)
