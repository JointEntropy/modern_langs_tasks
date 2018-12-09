#include <iostream>
#include <map>
using namespace std;





class FilmsManager
{
    map<int, string> movie_collection;
    map<int, int> states;
    int max_id;
    public:
        FilmsManager()
        {
            this->max_id = 0;
        }
        int add_movie(string name){
            int id_ = max_id;
            movie_collection.insert(pair<int, string> (id_, name));
            states.insert(pair<int, int> (id_, 0));
            max_id += 1;
            return id_;
        }
        void  print_collection()
        {
            for(auto iter = movie_collection.begin(); iter != movie_collection.end(); ++iter)
            {
                cout << iter->first << "  ::  " << iter->second << endl;
            }
        }
        void start_watch(int id)
        {
            states[id] = 1;
        }

        void finish_watch(int id)
        {
            states[id] = 2;
        }
        void show_current_watching()
        {
            cout << "You watching now:" << endl;
            for(auto iter = movie_collection.begin(); iter != movie_collection.end(); ++iter)
            {
                if(states[iter->first] == 1){
                    cout << iter->second << endl;
                }
            }
        }
        void show_id_less(int id)
        {
            cout << "Films with id below " << id << endl;
            for(auto it = movie_collection.begin(); it != movie_collection.lower_bound(id - 1); ++it)
            {
                cout << it->second << endl;
            }
        }
};


int main() 
{
    FilmsManager fm = FilmsManager();
    // init film collection
    fm.add_movie("Inception");
    int star_wars_id = fm.add_movie("Star Wars");
    fm.add_movie("Breaking bad");
    int shutter_island_id = fm.add_movie("Shutter Island");
    int coco_id = fm.add_movie("Coco");
    fm.add_movie("Treasure Planet");
    fm.print_collection();

    //
    fm.start_watch(star_wars_id);
    fm.start_watch(shutter_island_id);
    fm.start_watch(coco_id);
    fm.finish_watch(shutter_island_id);
    fm.show_current_watching();
    //

    fm.show_id_less(5);
    return 0;
}