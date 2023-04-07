import os


def main():
    # specify the path of the folder
    base_path = ".\\photo"
    # get all police station in to a list
    police_station_txt = open(os.path.join(base_path, "派出所.txt"), "r")
    police_station_list = []
    for line in police_station_txt.readlines():
        police_station_list.append(line.strip())
    police_station_txt.close()

    # get all police station's folder
    for police_station in police_station_list:
        police_station_path = os.path.join(base_path, police_station)
        cameras_txt = open(os.path.join(police_station_path, "監視器.txt"), "r")
        missing_list = []
        camera_list = []
        case = 0
        # get all camera in to a list and missing camera in to another list
        for line in cameras_txt.readlines():
            camera = line.strip()
            if camera:
                if "缺少" in camera:
                    case = 1
                    continue
                elif "監視器" in camera:
                    case = 2
                    continue
                match case:
                    case 1:
                        missing_list.append(camera)
                    case 2:
                        camera_list.append(camera)
        # remove missing camera from camera list
        camera_list = [val for val in camera_list if val not in missing_list]
        cameras_txt.close()

        # read files in the folder
        for root, dirs, files in os.walk(police_station_path):
            # remove already named files from camera list
            named_list = []
            print(camera_list)
            for file in files:
                if file.endswith(".jpg"):
                    file = file.replace(".jpg", "")
                    print(file)
                    if file in camera_list:
                        camera_list.remove(file)
                        named_list.append(file)
            print(camera_list)
            # rename files
            for file in files:
                if file.endswith(".jpg"):
                    file = file.replace(".jpg", "")
                    print(file)
                    if file in named_list:
                        continue
                    else:
                        new_name = camera_list.pop() + ".jpg"
                        print(new_name)
                        os.rename(os.path.join(root, file + ".jpg"), os.path.join(root, new_name))


if __name__ == "__main__":
    main()
