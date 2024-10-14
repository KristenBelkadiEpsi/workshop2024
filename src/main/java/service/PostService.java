package service;

import entity.Post;
import org.springframework.stereotype.Service;
import  repository.PostRepository;
import org.springframework.beans.factory.annotation.Autowired;
import  java.util.List;
@Service
public class PostService {
    @Autowired
    private PostRepository _postRepository;

    public  List<Post> GetAllPostTexts(){
        return _postRepository.findAll();
    }

    public Post SavePostText(Post _post){
        return _postRepository.save(_post);
    }
}
