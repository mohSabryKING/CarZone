

def make_all_list(Model_list,max_range):
      the_obj_list=[Model_list.objects.create(pk=x) for x in range(max_range)]
      print("creating a list\n:"+str(the_obj_list))
      return the_obj_list

def view_all_list(Model_list):return Model_list.objects.all()




def selected_marks(mark_item,made_list):
      selected_marks_list=[]
      for i in range(len(made_list)):
            print("adding item :"+str(mark_item))
            selected_marks_list.insert(i,mark_item)
      print("the created list \n"+str(selected_marks_list))
      return selected_marks_list